## REST Server with API Test

**The Project is one example to setup a payment RESTful sever (Django) and a complete test including functional and E2E (Postman API)**

**Features**  
There are the below features:
 - A complete transaction path from creating new account, creating new product item and then picking up these prodcuts in trolley and simulating payment
 - The database may be easily switched from sqlite3 to other DB such as mysql, SQLserver etc by changing the ([settings.py](woolworths_mock/woolworths_mock/settings.py)) 
 - Add clean function to clean the environment with one REST command, it may easily repeats the test for stress or performance purpose.


>[!NOTE]  
>The server is still under refining, the REST API will be improved in the future. 

**RESTAPI**  
> _GET all product items or POST a new product item_  
`/product/`                  
> _Query or update a product item such as "Rose Apple"_  
`/product/<object_id>`  
> _GET all trolly items or POST a new trolley item_        
`/trolley/`              
> _Query or update a trolly item_     
`/trolley/<object_id>`     
> _GET all trolly groups or POST a new trolley group_    
`/trolley_group/`           
> _Query or update a trolly group_   
`/trolley_group/<object_id>`   
> _Create a credit card record_   
`/credit_card/`    
> _Check the information of the credit card_          
`/credit_card/<object_id>`    
> _POST one transaction_    
`/transaction/`       
> _POST A new account_         
`/users/`                     


**Test**  
The project has completed the E2E test and functional test with Postman API
 - E2E Test: _A complete path from creating customer account to final transaction of a payment_  ([End-to-End_Tests.postman_collection.json](postman_api_test/end2end_test/End-to-End_Tests.postman_collection.json)) ([End-to-End_Tests.postman_test_run.json](postman_api_test/end2end_test/End-to-End_Tests.postman_test_run.json))
 ![E2E Test Result](/postman_api_test/end2end_test/e2e_test_result_capture.jpg) ![E2E Test Summary](/postman_api_test/end2end_test/e2e_test_summary_capture.jpg)
       
 - Functional Test: _A basic function test to verify the create/update/delete of a product item._  ([Functional_testing.postman_collection.json](postman_api_test/functional_api_test/Functional_testing.postman_collection.json)) ([Functional_testing.postman_test_run.json](postman_api_test/functional_api_test/Functional_testing.postman_test_run.json)) 
 ![Functional Test Result](/postman_api_test/functional_api_test/functional_api_test.jpg)

> [!TIP]  
> Any suggestions or questions please contact biao.yan612@gmail.com



