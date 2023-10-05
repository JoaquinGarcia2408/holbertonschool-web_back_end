import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
  .then((result) => {
    console.log(`${photoResult.body} ${userResult.firstName} ${userResult.lastName}`);
  })
  .catch((error) => {
    console.error('Signup system offline');
  });
}