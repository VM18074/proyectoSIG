import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { User } from './models/user';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private isLoggedIn: boolean = false;
  private currentUser: User | null = null;

  constructor() {}

  login(username: string, password: string): Observable<boolean> {
    // Reemplazar con lógica de login real
    this.isLoggedIn = true;
    this.currentUser = {
    id_usuario: 1,
    nombre_usuario: username,
    correo_electronico: 'example@email.com',
    usuario:username,
    password: password,
      // ... otras propiedades
    };
    return of(true);
  }

  isAuthenticated(): boolean {
    return this.isLoggedIn;
  }

  getCurrentUser(): User | null {
    return this.currentUser;
  }
}
