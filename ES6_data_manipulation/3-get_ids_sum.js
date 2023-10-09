export default function getStudentIdsSum(ListStudents) {
  return ListStudents.reduce((accumulator, student) => accumulator + student.id, 0);
}
