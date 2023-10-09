export default function updateStudentGradeByCity(listStudents, city, newGrades) {
  const filteredStudents = listStudents.filter(student => student.location === city);
  const updatedStudents = filteredStudents.map(student => {
    const newGrade = newGrades.find(grade => grade.studentId === student.id);
    return {
      ...student,
      grade: newGrade ? newGrade.grade : 'N/A',
    };
  });
  return updatedStudents;
};
