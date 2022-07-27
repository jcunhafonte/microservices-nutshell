package com.cloudbeds.channels.booking;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class BookingConfig {
    
    @Bean
    public BookingRepository bookingRepository() {
        return new BookingRepository();
    }
}