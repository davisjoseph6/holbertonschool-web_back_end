export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const listByCity = getListStudents.filter((student) => student.location === city);

  let stuGrade = 'N/A';
  const result = listByCity.map((obj) => {
    if (newGrades.some((s) => s.studentId === obj.id)) {
      const actualStudent = newGrades.filter((s) => s.studentId === obj.id);
      [stuGrade] = actualStudent;
    } else {
      stuGrade = 'N/A';
    }

    return ({
      id: obj.id,
      firstName: obj.firstName,
      location: obj.location,
      grade: typeof stuGrade === 'object' ? stuGrade.grade : 'N/A',
    });
  });

  return result;
}
