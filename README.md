## Capstone 1 - Project Proposal

1. What goal will your website be designed to achieve?  

    PSO PayScale is a website to crowdsource day rates for protected  
species observers so that they can negotiate fair pay.

2. What kind of users will visit your site? In other words, what is the demographic of
your users?   

    This is a very niche demographic. Protected Species Observers and Passive Acoustic Monitoring Operators worldwide.

3. What data do you plan on using? You may have not picked your actual API yet,  
which is fine, just outline what kind of data you would like it to contain.  

     Data itself will be collected from the users as they submit day rate information for each job they work on.  
     The API interaction would come either from a currency converter or from a mapping API.

4. In brief, outline your approach to creating your project (knowing that you may not
know everything in advance  
and that these details might change later). Answer
questions like the ones below, but feel free to add more information:  

     a. What does your database schema look like?  
    There would be at a minimum a user’s table and a jobs table.

    b. What kinds of issues might you run into with your API?  
    Until I pick one - this will have to stay pretty generic.  Most free API’s have a monthly limit to the number of calls  
    that can be made, which could turn into an issue once I actually launch PSO PayScale. 

    c. Is there any sensitive information you need to secure?  
A user’s name, password, and email + their job history.

    d. What functionality will your app include?  
Login, create a user profile and be able to add jobs.  There would also be an interactive map to click  
on the location of where you’re about to work that would show the high/low/and mean day rate for  
that area per each position (as long as data is available).

    e. What will the user flow look like?  
Before user’s can do anything they  
would need to sign up for an account and create a profile.  Then they would have access to the interactive map that 

    f. What features make your site more than CRUD? Do you have any stretch Goals?  
    I think the interactive map takes it further than basic CRUD.  I would eventually like to add a feature where a person  
    could print off a PDF of the data for a position/location in order to attach to whatever salary negotiations they’re  
    going through.  It may possibly be nice to turn it into a place for industry news / reviewing contracting companies  
    / posting jobs.


## Capstone 1 - Step 3 - API Choice and Schema

News API
https://currentsapi.services/en/docs/

Currency Converter
https://ratesapi.io/documentation/ or https://currentsapi.services/en/docs/


Draft Schema
<img src="https://github.com/petitepirate/capstoneOne/blob/master/Schema.png?raw=true">
