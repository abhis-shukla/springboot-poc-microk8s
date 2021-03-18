package metricsDemo;

import io.prometheus.client.Counter;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Random;

@RestController
public class SampleController {

    private static Random random = new Random();
    
    private static final Counter requestTotal = Counter.build()
        .name("my_sample_counter_demo")
        .labelNames("status")
        .help("A simple Counter to illustrate custom Counters in Spring Boot and Prometheus").register();

    @RequestMapping("/endpoint")
    public String endpoint() {
        if (random.nextInt(2) > 0) {
            requestTotal.labels("success").inc();
        } else {
            requestTotal.labels("error").inc();
        }
        return "What is CI/CD? This is probably one of the most frequently asked questions in any discussion of DevOps. Amid the rise and rise of CI/CD, it’s crucial to understand the process and then choose the right set of tools to fulfill technical requirements. In this article, I will provide insights into this notion, their benefits and how these practices are performed.";
    }
}
