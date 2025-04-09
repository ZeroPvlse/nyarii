package modules

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

var (
	ErrInvalidFile     = errors.New("file doesn't exist")
	ErrInvalidType     = errors.New("invalid option type")
	ErrFieldEmpty      = errors.New("this field can't be empty")
	ErrNegativeThreads = errors.New("threads cannot be negative")
)

type WebAttack struct {
	Target   string
	Wordlist string
	Threads  int
}

// IOHandler abstracts I/O operations to make code testable
type IOHandler interface {
	ReadInput() (string, error)
	WriteOutput(message string)
}

type DefaultIOHandler struct {
	reader *bufio.Reader
	writer io.Writer
}

func NewDefaultIOHandler() *DefaultIOHandler {
	return &DefaultIOHandler{
		reader: bufio.NewReader(os.Stdin),
		writer: os.Stdout,
	}
}

func (io *DefaultIOHandler) ReadInput() (string, error) {
	input, err := io.reader.ReadString('\n')
	if err != nil {
		return "", err
	}
	return strings.TrimSpace(input), nil
}

func (io *DefaultIOHandler) WriteOutput(message string) {
	fmt.Fprint(io.writer, message)
}

func NewWebAttackWithIO(io IOHandler) (*WebAttack, error) {
	io.WriteOutput("\nspecify target: ")
	target, err := io.ReadInput()
	if err != nil {
		return nil, err
	}

	target = strings.TrimSpace(target)
	if target == "" {
		io.WriteOutput(ErrFieldEmpty.Error() + "\n")
		return nil, ErrFieldEmpty
	}

	io.WriteOutput("\nwordlist path: ")
	wordlist, err := io.ReadInput()
	if err != nil {
		return nil, err
	}

	wordlist = strings.TrimSpace(wordlist)
	if wordlist == "" {
		io.WriteOutput(ErrFieldEmpty.Error() + "\n")
		return nil, ErrFieldEmpty
	}

	err = isValidFile(wordlist)
	if err != nil {
		io.WriteOutput(err.Error() + "\n")
		return nil, err
	}

	io.WriteOutput("\nthreads (default is 10): ")
	threadsInput, err := io.ReadInput()
	if err != nil {
		return nil, err
	}

	threadsInput = strings.TrimSpace(threadsInput)
	threads := 10 // default value
	if threadsInput != "" {
		threads, err = strconv.Atoi(threadsInput)
		if err != nil {
			io.WriteOutput(ErrInvalidType.Error() + "\n")
			return nil, ErrInvalidType
		}

	}
	attack := &WebAttack{
		Target:   target,
		Wordlist: wordlist,
		Threads:  threads,
	}
	if threads < 0 {
		return attack, ErrNegativeThreads
	}
	return attack, nil
}

func NewWebAttack() *WebAttack {
	attack, err := NewWebAttackWithIO(NewDefaultIOHandler())
	if err != nil {
		return nil
	}
	return attack
}

func isValidFile(wlist string) error {
	if wlist == "" {
		return ErrInvalidFile
	}

	if _, err := os.Stat(wlist); errors.Is(err, os.ErrNotExist) {
		return ErrInvalidFile
	}
	return nil
}
