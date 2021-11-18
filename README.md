# API_Testing

## Suchon site testing

| Test case ID | Test case name | Breif Description | Status |
| :---: | --- | --- | :---: |
| TC01 | test_get_all_people | The general test for test get_all_people API work correctly. | passed |
| TC02 | test_get_all_people_is_json_or_not | This test is used for check get_all_people API that is in json from. | passed |
| TC03 | test_get_had_appointment | The general test for get_people_by_date with correct date format. | passed |
| TC04 | test_get_not_had_appointment | The test for get the result when user enter the correct date format but do not have the appointment in the queue. | passed |
| TC05 | test_get_inexisted_appointment | Test the inexisted date | passed |
| TC06 | test_get_wrong_date_format | Test the wrong date format. The correct format must be only the integer | passed |
| TC07 | test_get_wrong_url_format | Test wrong url format | passed |

## Flameby testing

| Test case ID | Test case name | Breif Description | Status |
| :---: | --- | --- | :---: |
| TC01 | test_get_exist_user | Test the endpoint can get the correct user. | passed |
| TC02 | test_get_unexist_user | Test raising the error when fill the incorrect user_id in the endpoint. | passed |
| TC03 | test_valid_login | Test login is functional when enter the correct username and password. | passed |
| TC04 | test_invalid_password_login | Test raising error when enter the incorrect password. | passed |