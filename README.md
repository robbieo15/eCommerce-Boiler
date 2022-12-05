
# E-Commerce Boilerplate

The goal of this website is to create a general marketplace that can be repurposed.

## Features

- Vendor (Products)
- Contractor (Services)
- Consumer History
- Data Collection
- Payment Processing
- Automated Communications

## Functionality

Home Page

Products will fill the page with a search and log-in option.

Consumer Home

All previously searched items will auto-display. Also, there will be recommendations made based on other user data.

Owner Home

It will show low supply first. Allows the owner to see the amount of revenue for the day. Graphs will show the worst-selling items for the past 30 days (rolling).

Contractor Home

Calendar view through an API for installation and consultations.

System 

Will communicate automatically with customers when products are on their way. Will use an API to process payments as well.

## Data Model

User Model
- Username
- Password
- Email
- Log-In Time

Category Model
- Name

Products Model
- Image
- Description
- Title
- Category
- Cover Image
- Consumer Cost
- Profit per Item
- Created Date
- Supply Available

Vendor Model
- For Future

Contractor Model
- For Future

Data Collection Model
- Username
- Products Purchased
- Amount Purchased
- Time of Purchase

## Schedule

12/06
- Build User Model

12/08
- Build Products Model

12/13
- Create HTML Pages for Products, Users, and Admins

12/20
- Build method for purchasing Items
