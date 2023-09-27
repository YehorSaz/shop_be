import {Component, OnInit} from '@angular/core';
import {Dialog} from "@angular/cdk/dialog";
import {LoginFormComponent} from "../../components/login-form/login-form.component";
import {MatDialog} from "@angular/material/dialog";

@Component({
  selector: 'app-login-page',
  template: '',
})
export class LoginPageComponent implements OnInit {
  constructor(private dialog: MatDialog) {
  }

  ngOnInit(): void {
    this._openDialog()
  }

  private _openDialog():void{
    this.dialog.open(LoginFormComponent, {
      disableClose:true,
      hasBackdrop:true,
      enterAnimationDuration:'500ms',
      exitAnimationDuration:'500ms'
    })
  }

}
