## 📌 To-Do List Backend (Spring Boot + MySQL)  

### 📝 Description  
This is a simple **To-Do List backend** built using **Spring Boot, MySQL, and JPA**. It provides a **REST API** to manage tasks, including features to **add, update, delete, toggle, and filter tasks** based on completion status.  

### 🚀 Features  
✅ **CRUD Operations**: Create, Read, Update, and Delete tasks  
✅ **Task Completion Toggle**: Change task status (completed/incomplete)  
✅ **Filter Tasks**: Retrieve tasks based on completion status  
✅ **Spring Data JPA**: Efficient database interaction with Hibernate ORM  
✅ **MySQL Integration**: Stores tasks in a relational database  
✅ **Proper API Response Handling**: Uses `ResponseEntity` for status codes  

### 🛠️ Tech Stack  
- **Backend**: Spring Boot, Spring Data JPA, Lombok  
- **Database**: MySQL, Hibernate  
- **Tools**: Maven, Postman (for API testing)  

### 📡 API Endpoints  
| Method | Endpoint | Description | Request Body (if applicable) |  
|--------|---------|-------------|------------------|  
| **GET** | `/api/todo/tasks` | Get all tasks | ❌ |  
| **GET** | `/api/todo/tasks?toggle={true/false}` | Get completed/incomplete tasks | ❌ |  
| **GET** | `/api/todo/task?id={id}` | Get a task by ID | ❌ |  
| **POST** | `/api/todo/task/add` | Add a new task | `{ "task": "Task name" }` |  
| **PUT** | `/api/todo/task/update/{id}` | Update a task | `{ "task": "Updated Task", "completed": true/false }` |  
| **PUT** | `/api/todo/task/toggle/{id}` | Toggle task completion status | ❌ |  
| **DELETE** | `/api/todo/task/delete/{id}` | Delete a task | ❌ |  

### 📌 How to Use the REST API  
1. **Run the Spring Boot application** using `mvn spring-boot:run`  
2. Use **Postman** or a web browser to call the REST API endpoints  
3. Store and manage tasks using the API
