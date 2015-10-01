$fn = 40;
 difference() {
     union() {
         difference() {
             hull() {
                 cube([20.0, 37.0, 9.5], center=true);
                 translate([-9.25, 17.75, 0.0]) {
                     cylinder(r=1.5, h=9.5, center=true, $fn=20.0);
                }

                 translate([-9.25, -17.75, 0.0]) {
                     cylinder(r=1.5, h=9.5, center=true, $fn=20.0);
                }

                 translate([9.25, 17.75, 0.0]) {
                     cylinder(r=1.5, h=9.5, center=true, $fn=20.0);
                }

                 translate([9.25, -17.75, 0.0]) {
                     cylinder(r=1.5, h=9.5, center=true, $fn=20.0);
                }

            }

             cylinder(r=2.75, h=10.5, center=true);
        }

         translate([56.5, 0.0, 0.0]) {
             difference() {
                 cube([93.0, 30.0, 9.5], center=true);
                 union() {
                     cube([60.0, 5.5, 10.5], center=true);
                     translate([30.0, 0.0, 0.0]) {
                         cylinder(r=2.75, h=10.5, center=true);
                    }

                     translate([-30.0, 0.0, 0.0]) {
                         cylinder(r=2.75, h=10.5, center=true);
                    }

                }

            }

        }

    }

     translate([107.0, 0.0, 0.0]) {
         rotate(a=[0.0, 30.0, 0.0]) {
             translate([-46.5, 0.0, 2.0]) {
                 cube([93.0, 32.0, 9.5], center=true);
            }

        }

    }

}
