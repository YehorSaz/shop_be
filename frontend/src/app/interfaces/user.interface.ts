import {RoleEnum} from "../constants";

export interface IUser {
  id: string;
  email: string;
  is_active: boolean;
  last_login: Date;
  created_at: Date;
  updated_at: Date;
  profile?: {
    id: number;
    name: string;
    surname: string;
    phone: string;
    created_at: Date;
    updated_at: Date;
  }
  role: RoleEnum
}
