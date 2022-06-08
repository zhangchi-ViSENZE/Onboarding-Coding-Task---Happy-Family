import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { HttpClientModule } from "@angular/common/http";
import { FormsModule } from "@angular/forms";

import { AppComponent } from "./app.component";
import { ProductComponent } from "./components/product/product.component";
import { CheckAvailabilityComponent } from "./components/check-availability/check-availability.component";
import { PurchaseProductComponent } from "./components/purchase-product/purchase-product.component";

@NgModule({
  declarations: [
    AppComponent,
    ProductComponent,
    CheckAvailabilityComponent,
    PurchaseProductComponent,
  ],
  imports: [BrowserModule, HttpClientModule, FormsModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
