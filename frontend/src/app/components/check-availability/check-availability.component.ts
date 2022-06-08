import { Component, OnInit } from "@angular/core";
import { ProductService } from "../../product.service";
import { Product } from "src/app/Product";

@Component({
  selector: "app-check-availability",
  templateUrl: "./check-availability.component.html",
  styleUrls: ["./check-availability.component.css"],
})
export class CheckAvailabilityComponent implements OnInit {
  product: Product;
  errorMsg: Object;

  constructor(private productService: ProductService) {}

  ngOnInit() {}

  onSubmit(value): void {
    this.productService.getProduct(value.name).subscribe(
      (product: Product) => ((this.product = product), (this.errorMsg = null)),
      (error) => ((this.product = null), (this.errorMsg = error))
    );
  }
}
