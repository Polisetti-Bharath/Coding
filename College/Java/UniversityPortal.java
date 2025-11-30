class CourseFullException extends Exception {
    public CourseFullException(String message) {
        super(message);
    }
}

class Course {
    private String courseName;
    private int maxSeats;
    private int currentSeats;

    public Course(String courseName, int maxSeats) {
        this.courseName = courseName;
        this.maxSeats = maxSeats;
        this.currentSeats = 0;
    }

    public void registerStudent() throws CourseFullException {
        if (currentSeats < maxSeats) {
            currentSeats++;
            System.out.println("Student registered successfully for " + courseName +
                               ". Current seats: " + currentSeats + "/" + maxSeats);
        } else {
            throw new CourseFullException("Registration failed: The course '" + courseName +
                                          "' is already full (" + maxSeats + " seats).");
        }
    }
}

public class UniversityPortal {
    public static void main(String[] args) {
        Course javaCourse = new Course("Java Programming", 3);

        try {
            javaCourse.registerStudent();
            javaCourse.registerStudent();
            javaCourse.registerStudent();
            javaCourse.registerStudent();
        } catch (CourseFullException e) {
            System.err.println(e.getMessage());
        }
    }
}
