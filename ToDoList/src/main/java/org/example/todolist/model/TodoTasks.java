package org.example.todolist.model;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
public class TodoTasks {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String task;
//    @Column(columnDefinition = "BIT(1)")
    private boolean completed = false;
}
