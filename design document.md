# Onboard - happy family - design document

## Context
The wife said: "Please go to the store and buy a carton of milk and if they have eggs, get 12." The husband came back with 12 cartons of milk. The wife said: "why in the hell did you buy 12 cartons of milk." The husband responded: "They had eggs."

## User Story
As a husband who don't like go shopping, when my wife asks me to go and buy something
I would like to check if the product available or not before I go to the store
so that I don't waste my time and find the product everywhere and I buy the product correctly.  

## Acceptance Criteria
Given a store that sells milk cartons and eggs.
When husband makes a purchase.
Then he should get 1 milk carton if eggs sold out.
Then he should get 1 milk carton and 12 eggs if eggs are on stock.

## Design
### Architecture
![Architecture illustration](/Architecture%20Illustration.png)

**Basic structure**
- Frontend: Angular
- Backend: Python + Flask
- Database: SQLite


### Workflow
1. husband check the product stock remotely
2. if it's available,  buy the product

### API specification
| Method | Name | Description | Param | Response
| --- | --- | --- | --- | ---|
| GET | /store/milk | queries store for milk availability | - | quantity of milk available |
| GET | /store/eggs | queries store for eggs availability | - | quantity of eggs available |
| GET | /store/*AnyProductName* | queries store for *AnyProductName* availability | - | quantity of '*AnyProductName*' available |
| POST | /store/milk | buys milk from store | quantity (positive integer e.g. 1,2,3) | quantity of milk bought |
| POST | /store/milk | buys eggs from store | quantity (positive integer e.g. 1,2,3) | quantity of milk bought |
| POST | /store/*AnyProductName* | buys *AnyProductName* from store | quantity (positive integer e.g. 1,2,3) | quantity of *AnyProductName* bought |

#### **Constraints**
the API server must be up, and the service must be started

#### **Example request and respond**
| Method | Name | Description | Param | Response
| --- | --- | --- | --- | ---|
| GET | /store/milk | queries store for milk availability | - | {"name": "milk","quantity": 23} |
| GET | /store/eggs | queries store for eggs availability | - | {"name": "eggs","quantity": 92} |
| POST | /store/milk | buys milk from store | quantity=2 | {"name": "milk", "quantity": 2} |
| POST | /store/milk | buys eggs from store | quantity=30 | {"name": "eggs", "quantity": 30} |

#### **Error message**
| Description | Response |
| --- | ---- |
| Quantity is not a positive integer | { “error_code”: 400, “error_msg”: “Parameter must be a positive integer.” } |
| Quantity exceeds the current availability | { “error_code”: 400, “error_msg”: “Parameter must be smaller.” } |
| Product is not in the database | { “error_code”: 404, “error_msg”: “Product not found and Unsuccessful Purchase.” } |

## Implementation
### Frontend
> Components
> - **check-availability** : involves a form for user input and displays the availability of the wanted product
> - **purchase-product** : involves a form for user input and displays the successful purchase
> - **product** : product card involving product name and quantity

> Services
> - **product** : includes methods for CRUD request

### Backend
> Modules
> - **app** : includes main backend services besides the database related
> - **database** : includes services for setting up database and database CRUD

## Testing
 
## Execution
 
## References
[Angular Docs](https://angular.io/docs)

[How To Properly Construct A POST Requests In Angular](https://lokarithm.com/2020/12/30/angular-post-request-with-header-body-and-parameters/)

[Angular Project - angular-crash-2021](https://github.com/bradtraversy/angular-crash-2021)

[Flask Handling Application Errors](https://flask.palletsprojects.com/en/2.1.x/errorhandling/)