package org.example.todolist.service;

import org.example.todolist.dao.TodoRepo;
import org.example.todolist.model.TodoTasks;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class TodoService {
    @Autowired
    private TodoRepo todoRepo;

    public ResponseEntity<List<TodoTasks>> getAllTasks(){
        try{
            return new ResponseEntity<>(todoRepo.findAll(), HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<>(new ArrayList<>(),HttpStatus.BAD_REQUEST);
        }
    }

    public ResponseEntity<List<TodoTasks>> getAllTasksIfCompleted(boolean toggle){
        try{
            return new ResponseEntity<>(todoRepo.findAllByCompleted(toggle),HttpStatus.OK);
        }catch (Exception e){
            e.printStackTrace();
            return new ResponseEntity<>(new ArrayList<>(),HttpStatus.BAD_REQUEST);
        }
    }

    public ResponseEntity<TodoTasks> getTaskById(long id){
        try {
            return new ResponseEntity<>(todoRepo.findById(id).orElse(null), HttpStatus.OK);
        }catch(Exception e){
            e.printStackTrace();
            return new ResponseEntity<>(new TodoTasks(),HttpStatus.BAD_REQUEST);
        }
    }

    public ResponseEntity<TodoTasks> addTask(TodoTasks task){
        try {
            TodoTasks todoTasks = todoRepo.save(task);
            return new ResponseEntity<>(todoTasks, HttpStatus.CREATED);
        }catch (Exception e){
            e.printStackTrace();
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }
    }

    public ResponseEntity<String> deleteTask(long id) {
        try {
            if (todoRepo.existsById(id)) {
                todoRepo.deleteById(id);
                return new ResponseEntity<>("Task deleted successfully", HttpStatus.OK);
            } else {
                return new ResponseEntity<>("Task not found", HttpStatus.NOT_FOUND);
            }
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<>("Error deleting task", HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    public ResponseEntity<TodoTasks> updateTask(long id, TodoTasks task) {
        TodoTasks currTask = todoRepo.findById(id).orElse(null);

        if (currTask != null) {
            currTask.setTask(task.getTask());
            currTask.setCompleted(task.isCompleted());
            todoRepo.save(currTask);
            return new ResponseEntity<>(currTask, HttpStatus.OK);
        }

        return new ResponseEntity<>(HttpStatus.NOT_FOUND);
    }
}
