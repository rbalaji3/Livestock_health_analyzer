import { Component, OnInit } from '@angular/core';
import {data_model} from '../data_model';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'livestock-form',
  templateUrl: './livestock-form.component.html',
  styleUrls: ['./livestock-form.component.scss']
})
export class LivestockFormComponent implements OnInit {

  constructor(private http: HttpClient) { }

  ngOnInit() {

  }

  model = new data_model(0,0,0,0,0);
  response: any;

  submitted = false;

  onSubmit() {
    let api_url = 'http://127.0.0.1:5000/api';

    this.http.post<any>(api_url, this.model).subscribe(data => {
      this.response = data;
      this.submitted = true;

    })

  }

}
