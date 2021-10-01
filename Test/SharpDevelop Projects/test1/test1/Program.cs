/*
 * Created by SharpDevelop.
 * User: Microled
 * Date: 04/06/2019
 * Time: 16:59
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace test1
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine("Hello World!");
			
			for (int i=0;i<10;i++){
				Console.WriteLine("Hola {0}",i);
				                  
			}
			
			Console.Write("Press any key to continue . . . ");
			Console.ReadKey(true);
		}
	}
}