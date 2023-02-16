
import requests
key = "1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL"
ENDPOINT = "http://164.92.218.36:8080/api/addresses"

def test_can_create_address():
    payload = """<prestashop>
            <address>
                <id_customer></id_customer>
                <id_manufacturer></id_manufacturer>
                <id_supplier></id_supplier>
                <id_warehouse></id_warehouse>
                <id_country>1</id_country>
                <id_state></id_state>
                <alias>ksionz</alias>
                <company></company>
                <lastname>Shliakhta</lastname>
                <firstname>Olena</firstname>
                <vat_number></vat_number>
                <address1>Zalyvnyi 20</address1>
                <address2></address2>
                <postcode>37600</postcode>
                <city>Myrhorod</city>
                <other></other>
                <phone>661763661</phone>
                <phone_mobile>661763661</phone_mobile>
                <dni></dni>
                <deleted></deleted>
                <date_add></date_add>
                <date_upd></date_upd>
            </address>
        </prestashop>"""
    create_address_response = requests.post(ENDPOINT, auth=(key,""), data = payload)
    assert create_address_response.status_code == 201
    body = create_address_response.text
    address_id00 = body.split('</id>')
    address_id0 = address_id00[0].split('<id>')
    address_id = address_id0 [1][9:-3]
    get_created_address_response = requests.get(ENDPOINT + f'/{address_id}', auth=(key,""))
    assert get_created_address_response.status_code == 200

def test_can_update_address():
    payload = """<prestashop>
            <address>
                <id_customer></id_customer>
                <id_manufacturer></id_manufacturer>
                <id_supplier></id_supplier>
                <id_warehouse></id_warehouse>
                <id_country>1</id_country>
                <id_state></id_state>
                <alias>ksionz</alias>
                <company></company>
                <lastname>Shliakhta</lastname>
                <firstname>Olena</firstname>
                <vat_number></vat_number>
                <address1>Zalyvnyi 20</address1>
                <address2></address2>
                <postcode>37600</postcode>
                <city>Myrhorod</city>
                <other></other>
                <phone>661763661</phone>
                <phone_mobile>661763661</phone_mobile>
                <dni></dni>
                <deleted></deleted>
                <date_add></date_add>
                <date_upd></date_upd>
            </address>
        </prestashop>"""
    create_address_response = requests.post(ENDPOINT, auth=(key,""), data = payload)
    assert create_address_response.status_code == 201
    body = create_address_response.text
    address_id00 = body.split('</id>')
    address_id0 = address_id00[0].split('<id>')
    address_id = address_id0 [1][9:-3]
    new_address_payload = f"""<prestashop>
            <address>
                <id>{address_id}</id>
                <id_customer></id_customer>
                <id_manufacturer></id_manufacturer>
                <id_supplier></id_supplier>
                <id_warehouse></id_warehouse>
                <id_country>1</id_country>
                <id_state></id_state>
                <alias>ksionz</alias>
                <company></company>
                <lastname>Shliakhta</lastname>
                <firstname>Olena</firstname>
                <vat_number></vat_number>
                <address1>Zalyvnyi 20</address1>
                <address2></address2>
                <postcode>37600</postcode>
                <city>Kharkiv</city>
                <other></other>
                <phone>661763661</phone>
                <phone_mobile>661763661</phone_mobile>
                <dni></dni>
                <deleted></deleted>
                <date_add></date_add>
                <date_upd></date_upd>
            </address>
        </prestashop>"""
    update_address_response = requests.put(ENDPOINT + f'/{address_id}', auth=(key,""), data = new_address_payload)
    assert update_address_response.status_code == 200
    get_updated_address_response = requests.get(ENDPOINT + f'/{address_id}', auth=(key,""))
    assert get_updated_address_response.status_code == 200    
    new_body = new_address_payload
    new_body_city0 = new_address_payload.split('city>')
    new_body_city = new_body_city0 [1][:-2]
    updated_body = update_address_response.text
    updated_body_city0 = updated_body.split('city>')
    updated_body_city = updated_body_city0 [1][9:-5]
    assert updated_body_city == new_body_city
    
def test_can_delete_address():
    payload = """<prestashop>
            <address>
                <id_customer></id_customer>
                <id_manufacturer></id_manufacturer>
                <id_supplier></id_supplier>
                <id_warehouse></id_warehouse>
                <id_country>1</id_country>
                <id_state></id_state>
                <alias>ksionz</alias>
                <company></company>
                <lastname>Shliakhta</lastname>
                <firstname>Olena</firstname>
                <vat_number></vat_number>
                <address1>Zalyvnyi 20</address1>
                <address2></address2>
                <postcode>37600</postcode>
                <city>Myrhorod</city>
                <other></other>
                <phone>661763661</phone>
                <phone_mobile>661763661</phone_mobile>
                <dni></dni>
                <deleted></deleted>
                <date_add></date_add>
                <date_upd></date_upd>
            </address>
        </prestashop>"""
    create_address_response = requests.post(ENDPOINT, auth=(key,""), data = payload)
    assert create_address_response.status_code == 201
    body = create_address_response.text
    address_id00 = body.split('</id>')
    address_id0 = address_id00[0].split('<id>')
    address_id = address_id0 [1][9:-3]
    
    delete_address_response = requests.delete(ENDPOINT + f'/{address_id}', auth=(key,""))
    assert delete_address_response.status_code == 200
    
    get_deleted_address_response = requests.get(ENDPOINT + f'/{address_id}', auth=(key,""))
    assert get_deleted_address_response.status_code == 404