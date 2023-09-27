import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AuthRoutingModule } from './auth-routing.module';
import { LoginPageComponent } from './pages/login-page/login-page.component';
import { LoginFormComponent } from './components/login-form/login-form.component';
import {ReactiveFormsModule} from "@angular/forms";
import {MatCardModule} from "@angular/material/card";
import {MatInputModule} from "@angular/material/input";
import {MatButtonModule} from "@angular/material/button";


@NgModule({
  declarations: [
    LoginPageComponent,
    LoginFormComponent
  ],
  imports: [
    CommonModule,
    AuthRoutingModule,
    ReactiveFormsModule,
    MatCardModule,
    MatInputModule,
    MatButtonModule
  ]
})
export class AuthModule { }
