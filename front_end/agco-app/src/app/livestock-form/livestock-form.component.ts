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

  onSubmit() {
    console.log(this.model);

    this.http.post<any>('https://jsonplaceholder.typicode.com/posts', { title: 'Angular POST Request Example' }).subscribe(data => {
    })

  }

}
