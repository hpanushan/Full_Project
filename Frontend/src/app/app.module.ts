import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { JumbotronComponent } from './jumbotron/jumbotron.component';
import { FacebookComponent } from './facebook/facebook.component';
import { TwitterComponent } from './twitter/twitter.component';

const appRoutes: Routes = [
  { path: '', component: JumbotronComponent },
  { path: 'facebook', component: FacebookComponent },
  { path: 'twitter', component: TwitterComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    JumbotronComponent,
    FacebookComponent,
    TwitterComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes),
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
