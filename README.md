# a-ECG-diagnostic-System-software (Heart Disease Prediction System)
Manual Analysis of ECG signals is laborious and prone to error , even for specialist with manyy hours of xperience.

# STEPS TO RUN THIS PROJECT ON YOUR LOCAL MACHINE
    1) create and activate virtual environment 
         python -m venv virtual_env
        
         source virtual_env/bin/activate
    2) Then create a new directory and clone this 
        project files their

        mkdir directory_name

        cd directory_name

        git clone https://github.com/sandip-kumar-roy/a-ECG-diagnostic-System-software.git
        
        Cloning will start and all files will be
        ready inside your newly created directory

      
     3) Install all the required packages in order to go
        Smoothly
  
          pip install -r requirements.txt


     4) Then finally migrate the data's
   
         python manage.py makemigrations
   
         python manage.py migrate


      5) After successful migration type the following
       Command
 
        python manage.py runserver

And you are good to go..
          
# HOME PAGE
   front page of our website 
![image](https://user-images.githubusercontent.com/101457128/211147145-0c9ea027-bad2-484f-9af0-59d28ad3bb53.png)

  User Needs To Be login/register before using our Diagnostic Portal
![image](https://user-images.githubusercontent.com/101457128/211147201-2711fe95-fef2-4681-b9ef-2fe63c321d14.png)

# LOGIN PAGE
    Login page of our website
    Functionalities of this Login page

    1) If the User has Forgotten his/her password
       Can reset it again via Email OTP verification

    2) If user doesn't want to do the login part 
       Everytime he opens the website then he can use the
       Remember me option which basically stores the
       Cookie in that particular browser 

    3)If user enters invalid entry than a message
      Popup will appear saying **"Invalid Credentials"**

![image](https://user-images.githubusercontent.com/101457128/211147448-41b42d46-2cc3-42f9-878e-41dfe30a955d.png)

# AFTER LOGIN

   After login user will be redirected to home page 
   There then the Predict button will be enabled 
   And shows green colour on hover

   1) A logout navlink on navbar

   2)The profile page will be visible

   3) and Booking (appointments booking via PayPal)
      Will be visible on navbar

![image](https://user-images.githubusercontent.com/101457128/211147554-46b1a872-3945-4d0a-a9ab-0307a75d9f34.png)

# IF NEW USER HE/SHE NEEDS TO REGISTER

  **Registration page**
  We have embedded certain security checks like
  1) Username must be unique and if any previous
     User exists with that username then immediately
     a red message will show up saying 
     "Username already exists"

   2) password and confirm password must match 
   
   3) email id should be unique

   Note: if any of the above check doesn't satisfy 
         Then the register button will be disabled

![image](https://user-images.githubusercontent.com/101457128/211147640-1b589ee7-7db7-46f6-b667-9a9b600b2ea2.png)

     Security Features Of while registering

![image](https://user-images.githubusercontent.com/101457128/211147822-90c2c5d3-8052-4ac6-a3fd-63c15da671a8.png)

      Button Gets Disabled

![image](https://user-images.githubusercontent.com/101457128/211147861-57eadf2e-441e-451a-a0fe-14447a7db8cd.png)
      

![image](https://user-images.githubusercontent.com/101457128/211147898-a1f1974e-ef79-45dc-9bfb-38fb6dc98f7c.png)

      After successful passing of security check
      Button is enabled

![image](https://user-images.githubusercontent.com/101457128/211147924-f4c3dd8e-1066-4a88-9b2a-b1712eb5e9a7.png)
      
   
![image](https://user-images.githubusercontent.com/101457128/211147956-95bd80bb-5423-4397-942a-83fb0e96b1c6.png)

# PROFILE PAGE

 Profile demo
 
   **Lots of features is provided in the user
     Profile page

    1)user can view his/ her data with a profile pic 

    2)user can edit his/her profile data whenever he wants

    3)user can update his profile pic

    4)user can change his/her password

    5)user can sign out from the website

    6)user can delete hi/her account whenever he 
      Wants(once he/she does this that users whole
      Data will be removed from our's/admin's database

    7)Data safety is fully assured to the users

![image](https://user-images.githubusercontent.com/101457128/211148339-7369e386-8ee0-4f58-aaef-f80e68ede41c.png)

![image](https://user-images.githubusercontent.com/101457128/211148105-510fa397-2091-43af-9ce9-833fa10b61fd.png)

      Edit profile

    = All previous entered details will be as it is 
      On the form inputs which ensures that users doesn't
      Have to waste their time filling the whole form
      
       
![image](https://user-images.githubusercontent.com/101457128/211148494-d5f7839b-4df8-47e2-a44b-74cd985a6ac2.png)

      Change password

      User needs to enter email id, new password and confirm password
      If they are same then only user can submit unless the button will be disabled

![image](https://user-images.githubusercontent.com/101457128/211148512-d2ebce31-7cdd-49b7-9bcd-487d91419a17.png)
      
      prediction history
      
      Here user can check all his heart checkup details 
      
![image](https://user-images.githubusercontent.com/101457128/211148639-9268e273-52b5-4ace-b0f7-30240d4f3ce7.png)
       
       SIGNOUT

       User can log out from here also
![image](https://user-images.githubusercontent.com/101457128/211148677-3aab6e4f-a772-4d21-8908-54b6add2395b.png)

        DELETE ACCOUNT

        User can delete his account if he is not interested in staying
        With us anymore all the data will be erased linked by his user id

![image](https://user-images.githubusercontent.com/101457128/211148709-4af049c7-167a-48b4-bdd6-fc458cfa0bd4.png)

# BOOKING PART
     
    1)User can view all the details of his payment history 

    2)All. Details of failed and successful transaction

    3)Each Transaction generates a unique token/Invoice id

    4) All this info will be present under booking tab

![image](https://user-images.githubusercontent.com/101457128/211148730-f3ff632e-c38d-4551-92cf-bf6b43b8c0fe.png)

# PREDICTION
   
   1)User needs to fill the form using his previous
    Hospital checkup records regarding all the 12 
    attributes which will be used by our machine learning
    Model

   2)Hints are provided on the " i " buttons besides each labels

   2)Taking the 12 attributes our trained model will generate
     An output predicting the status of heart condition of
     the user as per his/her entered details 
   
  
![image](https://user-images.githubusercontent.com/101457128/211148754-a3eaa1ea-14bc-41d8-b2eb-d6d98b9fc34e.png)

# RESULTS

    Finally after submission of the form user will be
    Redirected to Result page to view his/her results
    
    1)Suppose by chance of user has done any mistake in his
      Form fillup so here he can preview his data using the
      "Preview your entered data" button
    2)There he/she can either edit / save the final time
    3) Then he would be able to view the results
    4)If the user is safe he/she should move to the safe
      Section of this page
    5) else he should immediately seek a doctor's
      Consultation
     6) No worries we have got our users covered
      We have provided their a "locate" button which 
      Helps them to locate remote cardio doctor 
![image](https://user-images.githubusercontent.com/101457128/211148842-ecf9a916-8485-4003-8031-3d5ae3483615.png)

![image](https://user-images.githubusercontent.com/101457128/211148872-e0907c19-5e7a-4da4-a3f5-dcdcc3fb41c8.png)

![image](https://user-images.githubusercontent.com/101457128/211148897-dfc20db4-6356-4384-a121-7d353077b72c.png)

![image](https://user-images.githubusercontent.com/101457128/211148924-56842b90-ddb2-423a-af50-d8df18fa3d99.png)

![image](https://user-images.githubusercontent.com/101457128/211148940-fe459049-e0a8-4e68-9247-3336cdd58962.png)

# HEALTHY TIPS

     Here we have provided some healthy tips which user can
     Apply in their daily life to see a change in their 
     Heart healthyness

![image](https://user-images.githubusercontent.com/101457128/211148987-6a42562c-b1a5-4ed1-92f0-d0f7858858d9.png)

# SEARCH FACILTY

    Here user can search based on city / state and get their desired
    Results which help them to locate the nearby doctors and can click on
    Any of the preferred doctor to book a slot
    
![image](https://user-images.githubusercontent.com/101457128/211149020-d084f1bc-629a-4712-a5f0-514de3c4de1f.png)

# BOOK A SLOT

     Now after clicking book slot user will redirected to booking 
     Page where he would be able to view the whole details of that particular
     Selected Doctor including the payment details 
     
     We have provided the amount details in INR but a user must have an
     PayPal account to go through our payment gateway

![image](https://user-images.githubusercontent.com/101457128/211149040-07e833dc-3ee8-4e34-ba5e-2c11d43ed050.png)

![image](https://user-images.githubusercontent.com/101457128/211149052-064ae0de-8beb-472e-9121-ee6ee9f43eb6.png)

![image](https://user-images.githubusercontent.com/101457128/211149075-8ce2434d-d53b-43b3-9692-9b7448a983af.png)


# FINAL PAYMENT USING PAYPAL


   Now after clicking on pay now button
   1) User will be redirected to PayPal payment gateway
      Where he/she had to do the final payment 

   2) User can also cancel his/her transaction during the payment
      If they wanna change their mind 

   3) They will be asked to enter their cards last three
      Digital


![image](https://user-images.githubusercontent.com/101457128/211149111-32abaed6-2ce7-4551-a790-2fe4f45d4c42.png)

![image](https://user-images.githubusercontent.com/101457128/211149161-5a2aa1f0-91a0-4561-be2f-689b8a1c7f86.png)

![image](https://user-images.githubusercontent.com/101457128/211149188-a5944bec-c176-4ce4-9c0d-c9621a101fff.png)

![image](https://user-images.githubusercontent.com/101457128/211149205-8851da8b-aeab-4de5-bb6a-1ead468eefe1.png)

![image](https://user-images.githubusercontent.com/101457128/211149216-34c0d0e3-3ced-4bf9-bc73-85762e69b468.png)

![image](https://user-images.githubusercontent.com/101457128/211149246-aae87568-dbe1-4d1c-9c72-a0ad480c2067.png)


# RESET PASSWORD

Suppose a user forgets his/her password and now wants to 
Login
Not to worry we have got your back covered

     1)we have provided the  Reset password facility which
       enables user to reset their password

     2)They will be asked to enter their username
       Then in the backend our system will search for that 
       particular username

     3) and if they finds that user then an OTP will be send to 
        their EMAIL ID and user will be asked to enter the 
        OTP which he/she recieved in his/her mail

     4)But if the user is not present then you will get a red notice
      Displaying that user doesn't exist 

![image](https://user-images.githubusercontent.com/101457128/211149280-c16e1ea3-b1c5-4b2f-add2-26bd7c828187.png)

![image](https://user-images.githubusercontent.com/101457128/211149292-ff2f073e-695b-40a4-8569-1690d1fc42b9.png)

![image](https://user-images.githubusercontent.com/101457128/211149300-696a0104-3b16-47fe-b61f-be72076711f6.png)

![image](https://user-images.githubusercontent.com/101457128/211149363-369dda45-7624-4f01-a450-5644176bd3f0.png)

![image](https://user-images.githubusercontent.com/101457128/211149374-355cf289-a781-4885-8146-462b035af92a.png)


# HERE ARE DEMO THE VIDEOS

# 1) Normal Overview Tour

https://user-images.githubusercontent.com/101457128/210917699-7735c0e0-bc49-43b0-a35c-0ce8626928fb.mp4

# profile page


# 2)Prediction form and search

https://user-images.githubusercontent.com/101457128/210919350-9a19b1ed-d78b-41c9-af8e-442214ac1e31.mp4

# 3)Payment gateway 

https://user-images.githubusercontent.com/101457128/210921191-c95feded-bdab-4616-8fc7-df8b2c995218.mp4

# 3)Otp verification for security purpose 

https://user-images.githubusercontent.com/101457128/210919444-44c56725-a1e5-4333-b8e2-2b17f02a36c9.mp4


# 4)Registration login and cookie

https://user-images.githubusercontent.com/101457128/210919936-7631e372-247c-4678-8e7f-6d001ad2101e.mp4


# 5)Normal tour after login different users

https://user-images.githubusercontent.com/101457128/210919996-f25a9d0d-285d-49d8-8e4a-9c7e7eb8ee10.mp4


# 6)Registration login security

https://user-images.githubusercontent.com/101457128/210921420-00cf7feb-2f9f-4df0-b7dd-3d258bbbdf55.mp4



