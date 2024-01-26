import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return new Promise((resolve) => {
    if (resolve) {
      resolve(
        Promise.all([uploadPhoto(), createUser()]).then((values) => {
          const photoBody = values[0].body;
          const userName = values[1].firstName;
          const userLastName = values[1].lastName;
          console.log(`${photoBody} ${userName} ${userLastName}`);
        }).catch(() => console.log('Signup system offline')),
      );
    }
  });
}
