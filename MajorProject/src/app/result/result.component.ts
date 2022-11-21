import { Component, Injectable, OnInit } from '@angular/core';
import {
  Storage,
  ref,
  uploadBytes,
  getDownloadURL,
  listAll,
} from '@angular/fire/storage';
import { AuthService } from '../authService/auth.service';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root',
})
@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css'],
})
export class ResultComponent implements OnInit {
  constructor(
    private http: HttpClient,
    private auth: AuthService,
    private storage: Storage
  ) {}

  file: any;
  files: string[] = [];
  faculty_file: any;
  ngOnInit(): void {
    this.getFiles();
  }
  data = {};
  call() {
    this.http
      .get('http://127.0.0.1:5000/api/Evaluate')
      .subscribe((result) => (this.data = result));
    // window.location.reload();
  }

  logout() {
    this.auth.logout();
  }

  uploadFilesFaculty(event: any) {
    this.faculty_file = event.target.files[0];
    console.log(this.faculty_file.name);
  }

  uploadFiles(event: any) {
    this.files = event.target.files;
    this.file = event.target.files[0];
    console.log(this.file.name);
  }
  addFacFile() {
    const fileRef = ref(this.storage, `files/${this.faculty_file.name}`);
    uploadBytes(fileRef, this.faculty_file)
      .then((x) => {
        console.log(x);
      })
      .catch((err) => {
        console.log(err);
      });
  }
  addFile() {
    for (var i = 0; i < this.files.length; i++) {
      this.file = this.files[i];

      const fileRef = ref(this.storage, `files/${this.file.name}`);
      uploadBytes(fileRef, this.file)
        .then((x) => {
          console.log(x);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }

  getFiles() {
    const filesRef = ref(this.storage, 'files');
    listAll(filesRef)
      .then(async (files) => {
        for (let file_one of files.items) {
          const url = await getDownloadURL(file_one);
          console.log(url);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }
}
