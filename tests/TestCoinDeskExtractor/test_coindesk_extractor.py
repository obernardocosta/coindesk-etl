#coding=utf-8
import json
import unittest
import src.CoinDeskExtractor.coindesk_extractor as coindesk_extractor


class TestCoinDeskExtractor(unittest.TestCase):
               
    def test_coindesk_status_code_exists(self):
        """Testando se existe um status_code no retorno"""
        ret = coindesk_extractor.main()
        self.assertTrue('status_code' in ret) 


    def test_coindesk_file_path_exists(self):
        """Testando se existe um file_path no retorno"""
        ret = coindesk_extractor.main()
        self.assertTrue('file_path' in ret) 


    def test_coindesk_content_type_exists(self):
        """Testando se existe um content_type no retorno"""
        ret = coindesk_extractor.main()
        self.assertTrue('content_type' in ret) 


    def test_coindesk_api_return(self):
        """Testando se o retorno da API é 200"""  
        ret = coindesk_extractor.main()
        self.assertTrue(ret['status_code'], 200)  


    def test_coindesk_api_json(self):
        """Testando se o content_type está correto, dado o que a API entrega"""
        ret = coindesk_extractor.main()
        self.assertTrue(ret['content_type'], 'application/javascript')  


    def test_coindesk_result_file_is_json(self):
        """Testando se o body de retorno é um dicionário (JSON)"""
        ret = coindesk_extractor.main()
        file_path = ret['file_path']
        with open(file_path, 'r') as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)


    def test_coindesk_result_file_keys(self):
        """Testando o body tem todas as chaves do nosso objeto template"""
        ret = coindesk_extractor.main()
        file_path = ret['file_path']
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        with open('tests/TestCoinDeskExtractor/coindesk_example_api.json', 'r') as f:
            mock_data = json.load(f)

        self.assertListEqual(
            sorted(data.keys()),
            sorted(mock_data.keys())
        )

if __name__ == '__main__':
    unittest.main()
