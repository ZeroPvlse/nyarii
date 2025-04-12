import unittest
from unittest.mock import patch, MagicMock, mock_open
import os
import sys
import io
from attacks.bruteforce import Init

class TestBruteforce(unittest.TestCase):
    
    @patch('builtins.print')
    @patch('attacks.bruteforce.prompt')
    def test_init_with_valid_inputs(self, mock_prompt, mock_print):
        
        mock_prompt.side_effect = [
            'http://example.com',  
            '/path/to/wordlist.txt',  
            '5'  
        ]
        
        bf = Init()
        
        self.assertEqual(bf.target, 'http://example.com')
        self.assertEqual(bf.wordlist_path, '/path/to/wordlist.txt')
        self.assertEqual(bf.threads, 5)
        
        
        self.assertEqual(mock_prompt.call_count, 3)
    
    @patch('builtins.print')
    @patch('attacks.bruteforce.prompt')
    def test_init_with_empty_target_then_valid(self, mock_prompt, mock_print):
        
        mock_prompt.side_effect = [
            '',  
            'http://example.com',  
            '/path/to/wordlist.txt',  
            '5'  
        ]
        
        bf = Init()
        
        self.assertEqual(bf.target, 'http://example.com')
        self.assertEqual(bf.wordlist_path, '/path/to/wordlist.txt')
        self.assertEqual(bf.threads, 5)
        self.assertEqual(mock_prompt.call_count, 4)
    
    @patch('builtins.print')
    @patch('attacks.bruteforce.prompt')
    def test_init_with_empty_wordlist_then_valid(self, mock_prompt, mock_print):
        
        mock_prompt.side_effect = [
            'http://example.com',  
            '',  
            '/path/to/wordlist.txt',  
            '5'  
        ]
        bf = Init()
        
        self.assertEqual(bf.target, 'http://example.com')
        self.assertEqual(bf.wordlist_path, '/path/to/wordlist.txt')
        self.assertEqual(bf.threads, 5)
        self.assertEqual(mock_prompt.call_count, 4)
    
    @patch('builtins.print')
    @patch('attacks.bruteforce.prompt')
    def test_init_with_invalid_threads_then_valid(self, mock_prompt, mock_print):
        
        mock_prompt.side_effect = [
            'http://example.com',  
            '/path/to/wordlist.txt',  
            'not-a-number',  
            '5'  
        ]
        bf = Init()
        self.assertEqual(bf.target, 'http://example.com')
        self.assertEqual(bf.wordlist_path, '/path/to/wordlist.txt')
        self.assertEqual(bf.threads, 5)
        self.assertEqual(mock_prompt.call_count, 4)
    
    @patch('builtins.print')
    @patch('attacks.bruteforce.prompt')
    def test_init_with_empty_threads_uses_default(self, mock_prompt, mock_print):
        
        mock_prompt.side_effect = [
            'http://example.com',  
            '/path/to/wordlist.txt',  
            ''  
        ]
        
        bf = Init()
        self.assertEqual(bf.target, 'http://example.com')
        self.assertEqual(bf.wordlist_path, '/path/to/wordlist.txt')
        self.assertEqual(bf.threads, 10)  
        self.assertEqual(mock_prompt.call_count, 3)
    
    @patch('attacks.bruteforce.Init.multithreaded_scan')  # mock the multithreaded_scan method
    @patch('builtins.print')
    @patch('os.path.abspath')
    @patch('os.path.expanduser')
    @patch('builtins.open', new_callable=mock_open, read_data="endpoint1\nendpoint2\nendpoint3")
    @patch('attacks.bruteforce.prompt')
    @patch('attacks.bruteforce.PathCompleter')
    def test_run_method(self, mock_path_completer, mock_prompt, mock_file, mock_expanduser, 
                      mock_abspath, mock_print, mock_multithreaded_scan):
        # reset mocks to clear any previous calls
        mock_expanduser.reset_mock()
        
        mock_prompt.side_effect = [
            'http://example.com',  
            '/path/to/wordlist.txt',  
            '5'  
        ]
        mock_expanduser.return_value = '/expanded/path/to/wordlist.txt'
        mock_abspath.return_value = '/absolute/path/to/wordlist.txt'
        
        path_completer_instance = MagicMock()
        mock_path_completer.return_value = path_completer_instance
        
        bf = Init()
        
        # reset mocks again before calling run(), to ensure we only count the calls from run()
        mock_expanduser.reset_mock()
        mock_abspath.reset_mock()
        
        # prevent multithreaded_scan from being called to avoid requests library calls
        bf.run()
        
        mock_expanduser.assert_called_once_with('/path/to/wordlist.txt')
        mock_abspath.assert_called_once_with('/expanded/path/to/wordlist.txt')
        mock_file.assert_called_once_with('/absolute/path/to/wordlist.txt', 'r')
        
        self.assertEqual(bf.words, ['endpoint1', 'endpoint2', 'endpoint3'])
    
    @patch('requests.get')
    @patch('builtins.print')
    @patch('attacks.bruteforce.prompt')
    def test_send_request_200_response(self, mock_prompt, mock_print, mock_get):
        
        mock_prompt.side_effect = [
            'http://example.com',  
            '/path/to/wordlist.txt',  
            '5'  
        ]
        
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        
        bf = Init()
        bf.words = ['admin', 'login', 'dashboard']
        bf.send_request()
        mock_get.assert_any_call('http://example.com/admin')
        mock_get.assert_any_call('http://example.com/login')
        mock_get.assert_any_call('http://example.com/dashboard')
        self.assertEqual(mock_get.call_count, 3)
    
    @patch('requests.get')
    @patch('builtins.print')
    @patch('attacks.bruteforce.prompt')
    def test_send_request_300_response(self, mock_prompt, mock_print, mock_get):
        
        mock_prompt.side_effect = [
            'http://example.com',  
            '/path/to/wordlist.txt',  
            '5'  
        ]
        
        mock_response = MagicMock()
        mock_response.status_code = 301
        mock_get.return_value = mock_response
        bf = Init()
        bf.words = ['redirect']
        bf.send_request()
        
        
        mock_get.assert_called_once_with('http://example.com/redirect')
    
    @patch('requests.get')
    @patch('builtins.print')
    @patch('attacks.bruteforce.prompt')
    def test_send_request_404_response(self, mock_prompt, mock_print, mock_get):
        
        mock_prompt.side_effect = [
            'http://example.com',  
            '/path/to/wordlist.txt',  
            '5'  
        ]

        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        bf = Init()
        bf.words = ['notfound']
        bf.send_request()
        mock_get.assert_called_once_with('http://example.com/notfound')
        

if __name__ == '__main__':
    unittest.main()
