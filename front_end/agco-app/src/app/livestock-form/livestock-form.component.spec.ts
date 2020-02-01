import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LivestockFormComponent } from './livestock-form.component';

describe('LivestockFormComponent', () => {
  let component: LivestockFormComponent;
  let fixture: ComponentFixture<LivestockFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LivestockFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LivestockFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
