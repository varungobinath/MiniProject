package org.example.todolist.controller;

import org.example.todolist.model.TodoTasks;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.example.todolist.service.TodoService;

import java.util.List;

@RestController
@RequestMapping("/api/todo")
public class TodoController {
    @Autowired
    private TodoService todoService;

    @GetMapping("/tasks") // /tasks && tasks?toggle={toggle}
    public ResponseEntity<List<TodoTasks>> getAllTask(@RequestParam(required = false) Boolean toggle){
        if(toggle==null) {
            return todoService.getAllTasks();
        }
        return todoService.getAllTasksIfCompleted(toggle);
    }

    @GetMapping("/task") //task?id={id}
    public ResponseEntity<TodoTasks> getTaskById(@RequestParam long id){
        ResponseEntity<TodoTasks> response = todoService.getTaskById(id);
        if(response.getBody()==null && response.getStatusCode()==HttpStatus.OK) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        return response;
    }

    @PostMapping("/task/add")
    public ResponseEntity<TodoTasks> addTask(@RequestBody TodoTasks task){
        return todoService.addTask(task);
    }

    @DeleteMapping("/task/delete/{id}")
    public ResponseEntity<String> deleteTask(@PathVariable long id){
        return todoService.deleteTask(id);
    }

    @PutMapping("/task/update/{id}")
    public ResponseEntity<TodoTasks> updateTask(@PathVariable long id, @RequestBody TodoTasks task){
        return todoService.updateTask(id,task);
    }

    @PutMapping("/task/toggle/{id}")
    private ResponseEntity<TodoTasks> toggleTask(@PathVariable long id){
        ResponseEntity<TodoTasks> response = todoService.getTaskById(id);
        if(response.getBody() == null) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        TodoTasks currTask = response.getBody();
        currTask.setCompleted(!currTask.isCompleted());
        return todoService.updateTask(id, currTask);
    }
}
