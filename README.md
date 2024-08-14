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
> _GET all product items or POST a new product item_  
#0969DA/product/                  
> _Query or update a product item such as "Rose Apple"_  
#0969DA/product/<object_id>  
> _GET all trolly items or POST a new trolley item_        
#0969DA/trolley/              
> _Query or update a trolly item_     
#0969DA/trolley/<object_id>     
> _GET all trolly groups or POST a new trolley group_    
#0969DA/trolley_group/           
> _Query or update a trolly group_   
#0969DA/trolley_group/<object_id> 
> _Create a credit card record_   
#0969DA/credit_card/    
> _Check the information of the credit card_          
#0969DA/credit_card/<object_id>   
> _POST complete one transaction_    
#0969DA/transaction/       
> _POST A new account_         
#0969DA/users                     


**Test**  
The project has completed the E2E test and functional test with Postman API
 - E2E Test: _A complete path from creating customer account to final transaction of a payment_  ([test_scripts](postman_api_test/end2end_test/End-to-End Tests.postman_collection.json)) ([test_result](postman_api_test/end2end_test/End-to-End Tests.postman_test_run.json))
 ![E2E Test Result](/postman_api_test/end2end_test/e2e_test_result_capture.jpg)
       
 - Functional Test: _A basic function test to verify the create/update/delete of a product item._  ([test_scripts](postman_api_test/functional_api_test/Functional testing.postman_collection.json)) ([test_result](postman_api_test/functional_api_test/Functional testing.postman_test_run.json)) 
 ![Functional Test Result](/postman_api_test/functional_api_test/functional_api_test.jpg)

> [!TIP]  
> Any suggestions or questions please contact biao.yan612@gmail.com



