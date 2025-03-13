package org.example.todolist.dao;

import org.example.todolist.model.TodoTasks;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface TodoRepo extends JpaRepository<TodoTasks,Long> {
    List<TodoTasks> findAllByCompleted(boolean completed);
}