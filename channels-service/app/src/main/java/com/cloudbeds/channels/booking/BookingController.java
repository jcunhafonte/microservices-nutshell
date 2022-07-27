package com.cloudbeds.channels.booking;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;


@RestController
@RequestMapping(value = "${api-prefix}/bookings", produces = MediaType.APPLICATION_JSON_VALUE)
@Tag(name = "bookings")
public class BookingController {
    
    private final BookingRepository BookingRepository;

    public BookingController(BookingRepository BookingRepository) {
        this.BookingRepository = BookingRepository;
    }

    @GetMapping
    @Operation(summary = "Get all bookings")
    public ResponseEntity<List<BookingDto>> getAll() {
        var bookings = BookingRepository.getAll();

        return new ResponseEntity<>(bookings, HttpStatus.OK);
    }

    @GetMapping("/{id}")
    @Operation(summary = "Get booking")
    public ResponseEntity<BookingDto> getById(@PathVariable Integer id) {
        var booking = BookingRepository.getById(id);

        return new ResponseEntity<>(booking, HttpStatus.OK);
    }
}