package com.cloudbeds.channels;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.beans.factory.annotation.Value;
import io.swagger.v3.oas.models.Components;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.info.License;

@SpringBootApplication
public class ChannelsServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(ChannelsServiceApplication.class, args);
	}

	@Bean
	public OpenAPI customOpenAPI(
		@Value("${openapi.project-title}") String title,
		@Value("${openapi.project-version}") String version,
		@Value("${openapi.project-description}") String description) {
		return new OpenAPI()
			.components(new Components())
			.info(new Info()
					.title(title)
					.version(version)
					.description(description)
			);
	}
}
