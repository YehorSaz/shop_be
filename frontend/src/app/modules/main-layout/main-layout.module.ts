import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';

import {MainLayoutRoutingModule} from './main-layout-routing.module';
import {HeaderComponent} from './components/header/header.component';
import {MainLayoutPageComponent} from './pages/main-layout-page/main-layout-page.component';
import {MatToolbarModule} from "@angular/material/toolbar";
import {MatDialogModule} from "@angular/material/dialog";


@NgModule({
  declarations: [
    HeaderComponent,
    MainLayoutPageComponent,
  ],
  imports: [
    CommonModule,
    MainLayoutRoutingModule,
    MatToolbarModule,
    MatDialogModule
  ]
})
export class MainLayoutModule { }
