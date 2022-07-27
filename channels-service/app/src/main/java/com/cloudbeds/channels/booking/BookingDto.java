package com.cloudbeds.channels.booking;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Builder;
import lombok.Data;

import java.util.UUID;

@Data
@Builder
@Schema(name = "Booking")
public class BookingDto {
    
    private Integer id;
    private String name;
    private String color;
    private String origin;
    private String price;
    private Integer quantity;
}