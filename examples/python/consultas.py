import os
import requests
from typing import Dict, Optional

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://consultas.cog.api.br/api/v1'


def check_status() -> Dict:
    """Check Telegram bot connection status"""
    print('=== Checking Telegram Bot Status ===\n')
    
    try:
        response = requests.get(
            f'{BASE_URL}/consulta/status',
            headers={'X-API-Key': API_KEY}
        )
        response.raise_for_status()
        
        data = response.json()
        print(f"Status: {data['status']}")
        print(f"Message: {data['message']}")
        print(f"Timestamp: {data['timestamp']}")
        
        return data
    except requests.exceptions.HTTPError as e:
        print(f'Error: {e.response.json() if e.response else str(e)}')
        raise
    except Exception as e:
        print(f'Error: {str(e)}')
        raise


def perform_query(query_type: str, data: str) -> Dict:
    """
    Perform a data query
    
    Args:
        query_type: Query type (cpf, nome, telefone, etc.)
        data: Data to query
    
    Returns:
        Query result dictionary
    """
    print(f'\n=== Query: {query_type.upper()} ===')
    print(f'Data: {data}\n')
    
    try:
        response = requests.get(
            f'{BASE_URL}/consulta',
            params={'type': query_type, 'dados': data},
            headers={'X-API-Key': API_KEY}
        )
        response.raise_for_status()
        
        result = response.json()
        
        if result.get('success'):
            print('✅ Query successful!')
            result_data = result.get('data', {})
            print(f"Type: {result_data.get('type', 'N/A')}")
            print(f"Query: {result_data.get('query', 'N/A')}")
            print(f"Timestamp: {result_data.get('timestamp', 'N/A')}")
            print('\n--- Result ---')
            print(result_data.get('resultado', 'No result'))
        else:
            print('❌ Query failed')
            print(f"Error: {result.get('error', 'Unknown')}")
            print(f"Message: {result.get('message', 'No message')}")
        
        return result
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            print('\n❌ Access Denied!')
            print('This endpoint requires an API key with daily limit > 500 requests.')
            print('Please upgrade to Unlimited or Bot plan.')
        elif e.response.status_code == 400:
            print('\n❌ Invalid Request!')
            error_data = e.response.json()
            print(error_data.get('message', 'Bad request'))
        else:
            print(f'\n❌ Error: {e.response.json() if e.response else str(e)}')
        raise
    except Exception as e:
        print(f'\n❌ Error: {str(e)}')
        raise


def query_by_cpf(cpf: str) -> Dict:
    """Query by CPF"""
    print('\n=== CPF Query ===')
    return perform_query('cpf', cpf)


def query_by_name(name: str) -> Dict:
    """Query by name"""
    print('\n=== Name Query ===')
    return perform_query('nome', name)


def query_by_phone(phone: str) -> Dict:
    """Query by phone"""
    print('\n=== Phone Query ===')
    return perform_query('telefone', phone)


def query_by_email(email: str) -> Dict:
    """Query by email"""
    print('\n=== Email Query ===')
    return perform_query('email', email)


def query_by_plate(plate: str) -> Dict:
    """Query by vehicle plate"""
    print('\n=== Vehicle Plate Query ===')
    return perform_query('placa', plate)


def query_by_cnpj(cnpj: str) -> Dict:
    """Query by CNPJ"""
    print('\n=== CNPJ Query ===')
    return perform_query('cnpj', cnpj)


def query_neighbors(cpf: str) -> Dict:
    """Query neighbors by CPF"""
    print('\n=== Neighbors Query ===')
    return perform_query('vizinhos', cpf)


def query_relatives(cpf: str) -> Dict:
    """Query relatives by CPF"""
    print('\n=== Relatives Query ===')
    return perform_query('parentes', cpf)


def query_addresses(cpf: str) -> Dict:
    """Query addresses by CPF"""
    print('\n=== Addresses Query ===')
    return perform_query('enderecos', cpf)


def query_jobs(cpf: str) -> Dict:
    """Query jobs by CPF"""
    print('\n=== Jobs Query ===')
    return perform_query('empregos', cpf)


def query_vaccines(cpf: str) -> Dict:
    """Query vaccines by CPF"""
    print('\n=== Vaccines Query ===')
    return perform_query('vacinas', cpf)


def query_benefits(cpf: str) -> Dict:
    """Query benefits by CPF"""
    print('\n=== Benefits Query ===')
    return perform_query('beneficios', cpf)


def query_score(cpf: str) -> Dict:
    """Query credit score by CPF"""
    print('\n=== Credit Score Query ===')
    return perform_query('score', cpf)


def query_cnh(cpf: str) -> Dict:
    """Query driver's license by CPF"""
    print('\n=== Driver License Query ===')
    return perform_query('cnh', cpf)


def main():
    """Example usage"""
    try:
        # Check status first
        check_status()
        
        # Example queries (replace with real data)
        
        # CPF query
        # query_by_cpf('00000000000')
        
        # Name query
        # query_by_name('João Silva')
        
        # Phone query
        # query_by_phone('11999999999')
        
        # Email query
        # query_by_email('example@email.com')
        
        # Vehicle plate query
        # query_by_plate('ABC1234')
        
        # CNPJ query
        # query_by_cnpj('00000000000000')
        
        # Advanced queries
        # query_neighbors('00000000000')
        # query_relatives('00000000000')
        # query_addresses('00000000000')
        # query_jobs('00000000000')
        # query_vaccines('00000000000')
        # query_benefits('00000000000')
        # query_score('00000000000')
        # query_cnh('00000000000')
        
        print('\n✅ Examples completed!')
        print('\nAvailable query types:')
        print('- cpf, nome, telefone, email')
        print('- placa, chassi, cnpj, cep')
        print('- titulo, pai, mae')
        print('- vizinhos, proprietario, empregos, vacinas')
        print('- beneficios, internet, parentes, enderecos')
        print('- obito, score, compras, cnh, funcionarios')
        
    except Exception:
        # Error already logged
        pass


if __name__ == '__main__':
    main()
