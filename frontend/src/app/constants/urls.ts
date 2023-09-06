import {environment} from "../../environments/environment";

const {API} = environment;

const auth = `${API}/auth`
const admin = `${API}/admin`
const courses = `${API}/courses`
const modules = `${API}/modules`


const urls = {
  auth: {
    login: auth,
    refresh: `${auth}/refresh`,
    me: `${auth}/me`,
    activate: (token: string): string => `${auth}/activate/${token}`,
    activateRequest: (userId: number): string => `${auth}/activateRequest/${userId}`,
  },

  admin: {
    managers: `${admin}/managers`,
    mentors: `${admin}/mentors`,
  },

  courses: {
    base: courses,
    names: `${courses}/names`,
    modules: (courseId: number): string => `${courses}/${courseId}/modules`,
    users: (courseId: number): string => `${courses}/${courseId}/users`,
  },

  modules
}
