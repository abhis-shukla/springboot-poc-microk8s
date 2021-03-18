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
        return "A CI/CD pipeline is a path for delivering a unit of change that starts from development to delivery. It helps organization to  automate steps in their software delivery process and allows application development teams to release software quickly.
 ";
    }
}
