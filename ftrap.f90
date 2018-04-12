subroutine trapezoidal(f, a, b, n)
  implicit none
  integer(I4B), intent(IN) :: n ! Number of trapezoids 
  real(SP), intent(IN) :: a, b ! lower and upper integration limits
  real(SP), intent(INOUT) :: h
  integer :: k     ! Iteration variable
  !result = 0.5*(f(a) - f(b))
  h = (b-a)/n 

  interface
     function f(x)
       real(SP), dimension(:), intent(in) :: x
       real(SP), dimension(size(x)) :: f
     end function f

  end interface

  
