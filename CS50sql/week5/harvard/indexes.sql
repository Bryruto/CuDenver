create index "enrollment_index" on "enrollments" ("student_id", "course_id");

create index "enrollment_index_student_id" on "enrollments" ("student_id");

create index "enrollment_index_course_id" on "enrollments" ("course_id");

create index "courses_index_department" on "courses" ("department");

create index "courses_index_number" on "courses" ("number");

create index "courses_index_semester" on "courses" ("semester");

create index "satisfies_index_course" on "satisfies" ("course_id");


