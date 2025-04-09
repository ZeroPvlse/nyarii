package modules

import (
	"bytes"
	"errors"
	"os"
	"path/filepath"
	"strings"
	"testing"
)

type MockIOHandler struct {
	InputResponses []string
	InputIndex     int
	OutputBuffer   *bytes.Buffer
	ShouldFailRead bool
}

func NewMockIOHandler(responses []string) *MockIOHandler {
	return &MockIOHandler{
		InputResponses: responses,
		InputIndex:     0,
		OutputBuffer:   &bytes.Buffer{},
		ShouldFailRead: false,
	}
}

func (m *MockIOHandler) ReadInput() (string, error) {
	if m.ShouldFailRead {
		return "", errors.New("simulated read failure")
	}

	if m.InputIndex >= len(m.InputResponses) {
		return "", errors.New("no more input responses")
	}
	response := m.InputResponses[m.InputIndex]
	m.InputIndex++
	return response, nil
}

func (m *MockIOHandler) WriteOutput(message string) {
	m.OutputBuffer.WriteString(message)
}

func (m *MockIOHandler) GetOutput() string {
	return m.OutputBuffer.String()
}

func TestIsValidFile(t *testing.T) {
	// Create a temporary file for testing
	tempDir := t.TempDir() // Using t.TempDir() for automatic cleanup
	tempFileName := filepath.Join(tempDir, "test-wordlist.txt")

	// Create the temporary file
	tempFile, err := os.Create(tempFileName)
	if err != nil {
		t.Fatalf("Failed to create temp file: %v", err)
	}
	tempFile.Close() // Close immediately as we only need it to exist

	// Create a subdirectory to test directory input
	subDirPath := filepath.Join(tempDir, "subdir")
	if err := os.Mkdir(subDirPath, 0755); err != nil {
		t.Fatalf("Failed to create test directory: %v", err)
	}

	tests := []struct {
		name        string
		filepath    string
		expectedErr error
	}{
		{
			name:        "Valid file",
			filepath:    tempFileName,
			expectedErr: nil,
		},
		{
			name:        "Invalid file",
			filepath:    "non-existent-file.txt",
			expectedErr: ErrInvalidFile,
		},
		{
			name:        "Valid directory (should pass isValidFile)",
			filepath:    subDirPath,
			expectedErr: nil, // isValidFile only checks existence, not file type
		},
		{
			name:        "Empty path",
			filepath:    "",
			expectedErr: ErrInvalidFile,
		},
		{
			name:        "File with special characters",
			filepath:    "te$t&file*?.txt",
			expectedErr: ErrInvalidFile,
		},
		{
			name:        "Very long path",
			filepath:    strings.Repeat("a/", 50) + "file.txt",
			expectedErr: ErrInvalidFile,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			err := isValidFile(tt.filepath)
			if !errors.Is(err, tt.expectedErr) {
				t.Errorf("isValidFile() error = %v, expected %v", err, tt.expectedErr)
			}
		})
	}
}

func TestNewWebAttackWithIO(t *testing.T) {
	// Create a temporary file for testing
	tempDir := t.TempDir()
	tempFileName := filepath.Join(tempDir, "test-wordlist.txt")

	// Create the temporary file
	tempFile, err := os.Create(tempFileName)
	if err != nil {
		t.Fatalf("Failed to create temp file: %v", err)
	}
	tempFile.Close()

	// Create a directory for testing
	dirPath := filepath.Join(tempDir, "testdir")
	if err := os.Mkdir(dirPath, 0755); err != nil {
		t.Fatalf("Failed to create test directory: %v", err)
	}

	tests := []struct {
		name           string
		inputs         []string
		expectedAttack *WebAttack
		expectedErr    error
		checkOutput    func(string) bool
		shouldFailRead bool
	}{
		{
			name:   "Valid inputs with default threads",
			inputs: []string{"https://example.com", tempFileName, ""},
			expectedAttack: &WebAttack{
				Target:   "https://example.com",
				Wordlist: tempFileName,
				Threads:  10,
			},
			expectedErr: nil,
			checkOutput: func(output string) bool {
				return strings.Contains(output, "specify target") &&
					strings.Contains(output, "wordlist path") &&
					strings.Contains(output, "threads (default is 10)")
			},
		},
		{
			name:   "Valid inputs with custom threads",
			inputs: []string{"https://example.com", tempFileName, "20"},
			expectedAttack: &WebAttack{
				Target:   "https://example.com",
				Wordlist: tempFileName,
				Threads:  20,
			},
			expectedErr: nil,
			checkOutput: nil,
		},
		{
			name:           "Empty target",
			inputs:         []string{"", tempFileName, ""},
			expectedAttack: nil,
			expectedErr:    ErrFieldEmpty,
			checkOutput: func(output string) bool {
				return strings.Contains(output, ErrFieldEmpty.Error())
			},
		},
		{
			name:           "Empty wordlist",
			inputs:         []string{"https://example.com", "", ""},
			expectedAttack: nil,
			expectedErr:    ErrFieldEmpty,
			checkOutput: func(output string) bool {
				return strings.Contains(output, ErrFieldEmpty.Error())
			},
		},
		{
			name:           "Invalid file path",
			inputs:         []string{"https://example.com", "non-existent-file.txt", ""},
			expectedAttack: nil,
			expectedErr:    ErrInvalidFile,
			checkOutput: func(output string) bool {
				return strings.Contains(output, ErrInvalidFile.Error())
			},
		},
		{
			name:           "Invalid threads input",
			inputs:         []string{"https://example.com", tempFileName, "invalid"},
			expectedAttack: nil,
			expectedErr:    ErrInvalidType,
			checkOutput: func(output string) bool {
				return strings.Contains(output, ErrInvalidType.Error())
			},
		},
		{
			name:   "Using directory as wordlist",
			inputs: []string{"https://example.com", dirPath, ""},
			expectedAttack: &WebAttack{
				Target:   "https://example.com",
				Wordlist: dirPath, // isValidFile only checks existence, not file type
				Threads:  10,
			},
			expectedErr: nil,
		},
		{
			name:   "Zero threads",
			inputs: []string{"https://example.com", tempFileName, "0"},
			expectedAttack: &WebAttack{
				Target:   "https://example.com",
				Wordlist: tempFileName,
				Threads:  0,
			},
			expectedErr: nil,
		},
		{
			name:   "Negative threads",
			inputs: []string{"https://example.com", tempFileName, "-5"},
			expectedAttack: &WebAttack{
				Target:   "https://example.com",
				Wordlist: tempFileName,
				Threads:  -5,
			},
			expectedErr: ErrNegativeThreads,
		},
		{
			name:   "Very large thread count",
			inputs: []string{"https://example.com", tempFileName, "999999"},
			expectedAttack: &WebAttack{
				Target:   "https://example.com",
				Wordlist: tempFileName,
				Threads:  999999,
			},
			expectedErr: nil,
		},
		{
			name:           "Input error during target prompt",
			inputs:         []string{},
			expectedAttack: nil,
			expectedErr:    errors.New("simulated read failure"),
			shouldFailRead: true,
		},
		{
			name:           "Whitespace-only target",
			inputs:         []string{"   ", tempFileName, "10"},
			expectedAttack: nil,
			expectedErr:    ErrFieldEmpty,
			checkOutput: func(output string) bool {
				return strings.Contains(output, ErrFieldEmpty.Error())
			},
		},
		{
			name:           "Whitespace-only wordlist",
			inputs:         []string{"https://example.com", "   ", "10"},
			expectedAttack: nil,
			expectedErr:    ErrFieldEmpty,
			checkOutput: func(output string) bool {
				return strings.Contains(output, ErrFieldEmpty.Error())
			},
		},
		{
			name:   "Max integer thread value",
			inputs: []string{"https://example.com", tempFileName, "2147483647"},
			expectedAttack: &WebAttack{
				Target:   "https://example.com",
				Wordlist: tempFileName,
				Threads:  2147483647, // INT_MAX
			},
			expectedErr: nil,
		},
		{
			name:           "Overflow integer thread value",
			inputs:         []string{"https://example.com", tempFileName, "9223372036854775808"}, // overflow int64
			expectedAttack: nil,
			expectedErr:    ErrInvalidType,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			mockIO := NewMockIOHandler(tt.inputs)
			mockIO.ShouldFailRead = tt.shouldFailRead

			attack, err := NewWebAttackWithIO(mockIO)

			// check error
			if tt.expectedErr != nil && err == nil {
				t.Errorf("Expected error %v, got nil", tt.expectedErr)
			} else if tt.expectedErr == nil && err != nil {
				t.Errorf("Expected no error, got %v", err)
			} else if tt.expectedErr != nil && err != nil {
				if tt.shouldFailRead && !strings.Contains(err.Error(), "simulated read failure") {
					t.Errorf("Expected error containing '%s', got '%s'", "simulated read failure", err.Error())
				} else if !tt.shouldFailRead && !errors.Is(err, tt.expectedErr) {
					t.Errorf("Expected error %v, got %v", tt.expectedErr, err)
				}
			}

			// check result
			if tt.expectedAttack == nil {
				if attack != nil {
					t.Errorf("Expected nil attack, got %+v", attack)
				}
			} else if attack == nil {
				t.Errorf("Expected non-nil attack, got nil")
			} else {
				if attack.Target != tt.expectedAttack.Target {
					t.Errorf("Target = %v, expected %v", attack.Target, tt.expectedAttack.Target)
				}
				if attack.Wordlist != tt.expectedAttack.Wordlist {
					t.Errorf("Wordlist = %v, expected %v", attack.Wordlist, tt.expectedAttack.Wordlist)
				}
				if attack.Threads != tt.expectedAttack.Threads {
					t.Errorf("Threads = %v, expected %v", attack.Threads, tt.expectedAttack.Threads)
				}
			}

			// check output if needed
			if tt.checkOutput != nil {
				output := mockIO.GetOutput()
				if !tt.checkOutput(output) {
					t.Errorf("Unexpected output: %s", output)
				}
			}
		})
	}
}
