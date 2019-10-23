import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ThrowStmt } from '@angular/compiler';

@Component({
  selector: 'app-facebook',
  templateUrl: './facebook.component.html',
  styleUrls: ['./facebook.component.css']
})
export class FacebookComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  onSubmit(facebook: NgForm) {
    console.log(facebook.value);
  }
}

