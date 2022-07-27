package com.cloudbeds.channels.booking;

import dev.codesoapbox.dummy4j.Dummy4j;

import java.util.List;

public class BookingRepository {
    
    private final Dummy4j dummy;

    private final Integer bookingsLength = 20;

    public BookingRepository() {
        this.dummy = new Dummy4j();
    }

    public List<BookingDto> getAll() {
        return dummy.listOf(this.bookingsLength, this::generateBooking);
    }

    public BookingDto getById(Integer id) {
        return generateBooking(id);
    }

    private BookingDto generateBooking(Integer... id) {
        return BookingDto.builder()
                .id(id.length > 0 ? id[0] : dummy.number().nextInt(1, this.bookingsLength))
                .name(dummy.lorem().word() + " " + dummy.lorem().word())
                .color(dummy.color().name())
                .origin(dummy.nation().country())
                .price(dummy.finance().priceBuilder().withCurrency("USD").build())
                .quantity(dummy.number().nextInt(1, 200))
                .build();
    }
}