## REST Server with API Test

**The Project is one example to setup a payment RESTful sever (Django) and a complete test including functional and E2E (Postman API)

**Features**  
There are the below features:
 - A complete transaction path from creating new account, creating new product item and then picking up these prodcuts in trolley and simulating payment
 - The database may be easily switched from sqlite3 to other DB such as mysql, SQLserver etc by changing the ([settings] (woolworths_mock/woolworths_mock/settings.py)).
 - Add clean function to clean the environment with one REST command, it may easily repeats the test for stress or performance purpose.


>[!NOTE]  
>The server is still under refining, the REST API will be improved in the future. 

**RESTAPI**
http://xxx.xx/product/                 _# GET all product items or POST a new product item_
http://xxx.xx/product/<object_id>      _# Query or update a product item such as "Rose Apple"_
http://xxx.xx/trolley/                 _# GET all trolly items or POST a new trolley item_
http://xxx.xx/trolley/<object_id>      _# Query or update a trolly item_ 
http://xxx.xx/trolley_group/           _# GET all trolly groups or POST a new trolley group_
http://xxx.xx/trolley_group/<object_id>_# Query or update a trolly group_ 
http://xxx.xx/credit_card/             _# Create a credit card record_
http://xxx.xx/credit_card/<object_id>  _# Check the information of the credit card_
http://xxx.xx/transaction/             _# POST complete one transaction_
http://xxx.xx/users                    _# POST A new account_


**Test**  
The project has completed the E2E test and functional test with Postman API
 - E2E Test: _A complete path from creating customer account to final transaction of a payment_  ([test_scripts](postman_api_test/end2end_test/End-to-End Tests.postman_collection.json)) ([test_result](postman_api_test/end2end_test/End-to-End Tests.postman_test_run.json))
       
 - Functional Test: _A basic function test to verify the create/update/delete of a product item._  ([test_scripts](postman_api_test/functional_api_test/Functional testing.postman_collection.json)) ([test_result](postman_api_test/functional_api_test/Functional testing.postman_test_run.json)) 


> [!TIP]  
> Any suggestions or questions please contact biao.yan612@gmail.com



