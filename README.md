# modern_health_django_graphql

This solution is in response to Modern Health's Technical Challenge using GRAPHQL, a non-rest implementation.

### Tech Stack

- Python3
- Django2
- GraphQL
- React

### Scope

We would like for you to create a backend for a simple tool that will enable the creation
of Programs, Weeks, and Pages.

Programs have 2 or more weeks
Programs have the following fields 
	- Name
	- Description
	- Image
	- Category
Weeks have 2 or more pages
Pages have the following fields
	- audio
	- video
	- article
	- form
	- question
The Program editor should follow CRUD operations for Programs, Weeks, and Pages.
Model should allow tracking of different pages, weeks, and programs
accomplished by the User.

### Instructions

`git clone https://github.com/aircert/modern_health_django_graphql.git` 
`cd modern_health_django_graphql`
`make`

### Access GraphQL Explorer

Click - [http://localhost:8000/graphql](http://localhost:8000/graphql?query=%23%20Create%20page%0A%0A%23%20mutation%20%7B%0A%23%20%20%20pageCreate(newPage%3A%20%7B%0A%23%20%20%20%20%20name%3A%20%22Page%206%22%2C%20%0A%23%20%20%20%20%20video%3A%20%22http%3A%2F%2Fgoogle.com%2Fvideo%22%2C%0A%23%20%20%20%09audio%3A%20%22http%3A%2F%2Fgoogle.com%2Faudio%22%2C%0A%23%20%20%20%20%20form%3A%20%22http%3A%2F%2Fgoogle.com%2Fform%22%2C%0A%23%20%20%20%20%20question%3A%20%22http%3A%2F%2Fgoogle.com%2Fquestion%22%2C%0A%23%20%20%20%20%20article%3A%20%22http%3A%2F%2Fgoogle.com%2Farticle%22%0A%23%20%20%20%7D)%20%7B%0A%23%20%20%20%20%20page%20%7B%0A%23%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20complete%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Create%20Week%0A%23%20mutation%20%7B%0A%23%20%20%20weekCreate(newWeek%3A%20%7B%0A%23%20%20%20%20%20pages%3A%20%5B6%2C%205%5D%2C%0A%23%20%20%20%20%20name%3A%20%22Week%204%22%0A%23%20%20%20%7D)%20%7B%0A%23%20%20%20%09week%20%7B%0A%23%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20pages%20%7B%0A%23%20%20%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20%7D%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Delete%20Program%0A%23%20mutation%20%7B%0A%23%20%20%20programDelete(id%3A%202)%20%7B%0A%23%20%20%20%20%20program%20%7B%0A%23%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Create%20Program%0A%23%20mutation%20%7B%0A%23%20%20%20programCreate(newProgram%3A%20%7B%0A%23%20%20%20%20%20name%3A%20%22Mindful%20Communication%22%2C%0A%23%20%20%20%20%20description%3A%20%22Minfully%20communicate%20with%20coworkers%22%2C%0A%23%20%20%20%20%20weeks%3A%20%5B3%2C4%5D%2C%0A%23%20%20%20%20%20progress%3A%200%0A%23%20%20%20%7D)%20%7B%0A%23%20%20%20%20%20program%20%7B%0A%23%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20description%0A%23%20%20%20%20%20%20%20progress%0A%23%20%20%20%20%20%20%20image%0A%23%20%20%20%20%20%20%20weeks%20%7B%0A%23%20%20%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20%20%20pages%20%7B%0A%23%20%20%20%20%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20%20%20%20%20complete%0A%23%20%20%20%20%20%20%20%20%20%7D%0A%23%20%20%20%20%20%20%20%7D%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%20%20errors%20%7B%0A%23%20%20%20%20%20%20%20messages%0A%23%20%20%20%20%20%20%20field%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Get%20All%20Weeks%20%0A%23%20query%20%7B%0A%23%20%20%20allWeeks%20%7B%0A%23%20%20%20%20%20id%0A%23%20%20%20%20%20name%0A%23%20%20%20%20%20pages%20%7B%0A%23%20%20%20%20%20%20%20name%0A%23%20%20%20%20%20%20%20complete%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Get%20all%20pages%0A%0A%23%20query%20%7B%0A%23%20%20%20allPages%20%7B%0A%23%20%20%20%20%20id%0A%23%20%20%20%20%20name%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%0A%23%20Get%20all%20programs%2C%20weeks%2C%20and%20pages%20for%20each%0Aquery%20%7B%0A%20%20allPrograms%20%7B%0A%20%20%20%20id%0A%20%20%20%20name%0A%20%20%20%20description%0A%20%20%20%20progress%0A%20%20%20%20image%0A%20%20%20%20weeks%20%7B%0A%20%20%20%20%20%20id%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20pages%20%7B%0A%20%20%20%20%20%20%20%20id%20%0A%20%20%20%20%20%20%20%20name%0A%20%20%20%20%20%20%20%20complete%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A%0A%23%20Update%20a%20program%20by%20weeks%20%0A%23%20mutation%20%7B%0A%23%20%20%20programUpdate(newProgram%3A%20%7Bid%3A%202%2C%20weeks%3A%20%5B1%2C2%2C3%2C4%5D%7D)%20%7B%0A%23%20%20%20%20%20program%20%7B%0A%23%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20weeks%20%7B%0A%23%20%20%20%20%20%20%20%20%20id%0A%23%20%20%20%20%20%20%20%7D%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D%0A%0A%23%20Update%20a%20pages%20progress%20to%20complete%0A%23%20mutation%20%7B%0A%23%20%20%20pageUpdate(newPage%3A%20%7Bid%3A%201%2C%20complete%3A%20true%7D)%20%7B%0A%23%20%20%20%20%20page%20%7B%0A%23%20%20%20%20%20%09id%0A%23%20%20%20%20%20%20%20complete%0A%23%20%20%20%20%20%20%20dateModified%0A%23%20%20%20%20%20%20%20dateCreated%0A%23%20%20%20%20%20%7D%0A%23%20%20%20%7D%0A%23%20%7D)

Create page

mutation {
  pageCreate(newPage: {
    name: "Page 6", 
    video: "http://google.com/video",
  	audio: "http://google.com/audio",
    form: "http://google.com/form",
    question: "http://google.com/question",
    article: "http://google.com/article"
  }) {
    page {
      id
      complete
    }
  }
}

Create Week
mutation {
  weekCreate(newWeek: {
    pages: [6, 5],
    name: "Week 4"
  }) {
  	week {
      id
      name
      pages {
        name
      }
    }
  }
}

Delete Program
mutation {
  programDelete(id: 2) {
    program {
      id
    }
  }
}

Create Program
mutation {
  programCreate(newProgram: {
    name: "Mindful Communication",
    description: "Minfully communicate with coworkers",
    weeks: [3,4],
    progress: 0
  }) {
    program {
      id
      name
      description
      progress
      image
      weeks {
        id
        name
        pages {
          id
          name
          complete
        }
      }
    }
    errors {
      messages
      field
    }
  }
}

Get All Weeks 
query {
  allWeeks {
    id
    name
    pages {
      name
      complete
    }
  }
}

Get all pages

query {
  allPages {
    id
    name
  }
}


Get all programs, weeks, and pages for each
query {
  allPrograms {
    id
    name
    description
    progress
    image
    weeks {
      id
      name
      pages {
        id 
        name
        complete
      }
    }
  }
}

Update a program by weeks 
mutation {
  programUpdate(newProgram: {id: 2, weeks: [1,2,3,4]}) {
    program {
      id
      weeks {
        id
      }
    }
  }
}

Update a pages progress to complete
mutation {
  pageUpdate(newPage: {id: 1, complete: true}) {
    page {
    	id
      complete
      dateModified
      dateCreated
    }
  }
}

### Check Frontend 
	- Navigate to http://localhost:8000