export default function getListStudentIds(array) {
  if (Array.isArray(array)) {
    const object_list = array.map((student) => student.id);
    return object_list;
    }
    return [];
}
