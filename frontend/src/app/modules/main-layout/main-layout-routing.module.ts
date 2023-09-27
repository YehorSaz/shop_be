import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {MainLayoutPageComponent} from "./pages/main-layout-page/main-layout-page.component";

const routes: Routes = [
  {
    path: '', component: MainLayoutPageComponent, children: [
      {
        path:'', redirectTo:'auth', pathMatch:'full'
      },
      {
        path: 'auth', loadChildren: () => import('./modules/auth/auth.module').then(m => m.AuthModule)
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainLayoutRoutingModule {
}
