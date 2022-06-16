import { Injectable } from "@angular/core";
import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
  HttpParams,
} from "@angular/common/http";
import { Observable, throwError } from "rxjs";
import { catchError } from "rxjs/operators";
import { Product } from "./Product";

@Injectable({
  providedIn: "root",
})
export class ProductService {
  private baseurl = "http://127.0.0.1:5000";

  private handleError(error: HttpErrorResponse) {
    if (error.status === 0) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error("An error occurred:", error.error);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong.
      console.error(
        `Backend returned code ${error.status}, body was: `,
        error.error
      );
    }
    // Return an observable with a user-facing error message.
    return throwError(error.error.error_msg);
  }

  constructor(private http: HttpClient) {}

  getProduct(productName: string) {
    return this.http
      .get<Product>(this.baseurl + "/store/" + productName)
      .pipe(catchError(this.handleError));
  }

  buyProduct(product: Product) {
    const httpOptions = {
      headers: new HttpHeaders({
        "Content-Type": "application/json",
      }),
      params: new HttpParams().append("quantity", product.quantity.toString()),
    };
    console.log({ quantity: product.quantity });
    return this.http
      .post<Product>(
        this.baseurl + "/store/" + product.name,
        null,
        httpOptions
      )
      .pipe(catchError(this.handleError));
  }
}
