![main.png](./img/fridge.png)

# Unit 3: Fridge Tracker Software

# Criteria A: Planning

## Problem definition

$\qquad$ My client is a Residential Assistant (RA) of a house in a boarding International Baccalaureate (IB) school. As an RA of the house, she is responsible to solve any problems that comes up in the house. She wants an application to solve a running problem that has bothered her and her house members for the past year. The problem is with the fridge of the house. The fridge is always messy and filled with expired products. Because of the amount of expired products in the fridge, the fridge smells extremely bad and creates a negative house environment and is also a health hazard. A few days ago someone ate expired fish and got very sick. Additionally, the house members also have a hard time remembering which food is theirs and end up eating other people's food. This pisses the actual food owners off and creates a lot of fights in the house. My client wants to put an end to all by having a fridge tracker app. 

$\qquad$ The fridge tracker app would allow my client and her housemates to add items they own and add information like expiry_date and quantity. The application would also let my client and her housemates to view all items and who own them. This would solve the problem of people eating other people's food. The application would also send warning messages to logged in users when their items are going to expire in the next 7 days or when quantity is low. This will let them be aware of the expiry date and deal with the food item in a timely and proper manner. This will solve the bad smelling and health hazard issues. 

## Rationale

$\qquad$ The application will be a dynamic application meaning that it will display personalized notifications of the user. Due to this, the application needs a login system. The application must also hash passwords as 

## Success Criteria
1. The application has a login system where users can login and register using username, email, and password 
2. The application provides a screen to let logged in user view, edit, and delete items in the fridge
3. The application gives notifications when an item is about to expire in the next 7 days and changes the color of such items on the table to red
4. The application fridge view has filters that can let you categorize the items based on type of item: meat, sweets, drinks, fruits & veggies, dairy
5. The application fridge view has filters that can let you categorize items based on owner
6. The application gives notifications when an item's quantity is less than 10% of normal and changes the color of such items on the table to orange
7. The application automatically adds the logged in user as owner when adding a new item to the fridge
<!-- show logs? -->

## Meeting with client to discuss Success Criteria

![main.png](./img/client_meeting.jpeg)

# Criteria B: Design

<!-- ## System Diagram **SL** -->
<!-- ![](sysdim_sl.png) -->

<!-- **Fig.1** shows the system diagram for the proposed solution (**SL**). The indoor variables will be measured using an Arduino microprocessor and the sensor DHT11 conencted to the local computer (Laptop) located inside a room. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.147/readings```. The local values are stored in a CSV database locally. -->

<!-- ![](sysdim_hl.png)

**Fig.2** shows the system diagram for the proposed solution (**HL**). The indoor variables will be measured using a Raspberry PI and four DHT11 sensors located inside a room. Four sensors are used to determine more precisely the physical values and include measurement uncertainty. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.147/readings```. The local values are stored in a CSV database locally and POST to the server using the API and TOKEN authentication. A laptop computer is used for remotely controlling the local Rasberry Pi using a Dekptop sharing application (VNC Viewer). (Optional) Data from the local raspberry is downloaded to the laptop for analysis and processing. -->


## Record of Tasks
| **Task No.** |  **Planned Action** |          **Planned Outcome**         | **Time Estimate** | **Target Completion Date** | **Criterion** |
|:------------:|:-------------------:|:------------------------------------:|:-----------------:|:--------------------------:|:-------------:|
|       1      | Meeting with client | Start collecting context for problem |       6 min       |        7th Feb 2023        |       A       |
|       2      | Create problem defination | Have the client's problem defined |       25 min       |        9th Feb 2023        |       A       |
|       3      | Create success criterias | Have the success criteria of the application that solved the client's problems |       1 hours       |        15th Feb 2023        |       A       |
|       4      | Present success criteria to client | Have the success criteria of the application aprooved by the client |       10 minutes       |        28th Feb 2023        |       A       |
|       5      | Write rationale | Have the tools used in the application explained and justified |       90 minutes       |        28th Feb 2023        |       A       |


## Test Plan

# Criteria C: Development

## List of techniques used

## Development


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration


<!-- OWNER ????????? -->
<!-- Client meeting #2 -->
<!-- add expiry date for products
change color of product if expired
23rd feb -->

<!-- Client meeting #1 -->

<!-- Tracker for fridge
    add items in the frigeq
    edit items in the fridge
    delete items from the fridge

Items should have quanity 
Items type:
    sweet
    veggies
    meat
    drinks -->

<!-- 
record of task

first planning. meeting with client
start collecting context of the problm
6 min 
7 feb
A
 -->